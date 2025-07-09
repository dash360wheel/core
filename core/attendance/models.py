from datetime import timedelta

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from pip._internal.utils import datetime


# ***************************************************************
#  Developer:    Brou Yao
#
#  Project #:    GroupScolaireDash360
#
#  File Name:    AttendanceRecord.py
# Imported models: ContentType, GenericForeignKey, User (via settings.AUTH_USER_MODEL)
#
#  Due Date:     OCT 20, 2024
#
#  Description:  Defines generic AttendanceRecord model for tracking
#                attendance for any object (course, event, activity, etc.).
#
# ***************************************************************

class AttendanceRecord(models.Model):

    """# Link to any object: course, event, club, etc.
    # ***************************************************************
    #  Developer:    Brou Yao
    #
    #  Project #:    GroupScolaireDash360
    # Imported models: ContentType, GenericForeignKey, User (via settings.AUTH_USER_MODEL)
    #
    #  File Name:    AttendanceRecord.py
    #
    #  Due Date:     OCT 20, 2024
    #
    #  Description:  Defines generic AttendanceRecord model for tracking
    #                attendance for any object (course, event, activity, etc.).
    #
    # ***************************************************************"""

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    attended_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    break_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    status = models.CharField(choices=[
        ("present", "Present"),
        ("absent", "Absent"),
        ("late", "Late"),
        ("left_early", "Left Early"),
        ("excused", "Excused")
    ], max_length=20)

    remarks = models.TextField(blank=True)
    marked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="attendance_marked", null=True, blank=True, on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def attendance_duration(self):
        """
        Calculates the duration of attendance for this record.
        Returns the duration between start and end time, minus break time if applicable.
        Returns a timedelta object.
        """
        if self.start_time and self.end_time:
            dt_start = datetime.combine(self.date, self.start_time)
            dt_end = datetime.combine(self.date, self.end_time)
            duration = dt_end - dt_start

            # Subtract break time if available
            if self.break_time:
                dt_break = datetime.combine(self.date, self.break_time)
                duration -= timedelta(hours=dt_break.hour, minutes=dt_break.minute)
            return duration
        return timedelta(0)

        # ========== AGGREGATE METHODS ==========


    @classmethod
    def total_days_present(cls, user):
        """
        Returns the total number of days the user was marked as 'present'.
        """
        return cls.objects.filter(user=user, status="present").count()


    @classmethod
    def total_lates(cls, user):
        """
        Returns the total number of times the user was marked as 'late'.
        """
        return cls.objects.filter(user=user, status="late").count()


    @classmethod
    def total_left_early(cls, user):
        """
        Returns the total number of times the user was marked as 'left_early'.
        """
        return cls.objects.filter(user=user, status="left_early").count()


    @classmethod
    def total_absences(cls, user):
        """
        Returns the total number of times the user was marked as 'absent'.
        """
        return cls.objects.filter(user=user, status="absent").count()


    @classmethod
    def attendance_percentage(cls, user):
        """
        Calculates the attendance percentage for the given user:
        (number of presents / total records) * 100.
        Returns 0 if user has no attendance records.
        """
        total = cls.objects.filter(user=user).count()
        if total == 0:
            return 0
        present = cls.objects.filter(user=user, status="present").count()
        return round((present / total) * 100, 2)


    @classmethod
    def total_work_time(cls, user):
        """
        Calculates the total attendance duration for all 'present' records for a user.
        Returns the sum as a timedelta object.
        """
        total_duration = timedelta()
        records = cls.objects.filter(user=user, status="present")
        for record in records:
            dur = record.attendance_duration()
            if dur:
                total_duration += dur
        return total_duration


    @classmethod
    def average_daily_work_time(cls, user):
        """
        Calculates the average daily attendance duration for all 'present' records for a user.
        Returns a timedelta object.
        """
        records = cls.objects.filter(user=user, status="present")
        count = records.count()
        if count == 0:
            return timedelta()
        return cls.total_work_time(user) / count


    @classmethod
    def daily_summary(cls, user, date):
        """
        Returns a dictionary summarizing a user's attendance for a given date.
        Includes status, duration, and remarks.
        If no record exists, returns status 'absent' and duration 0.
        """
        try:
            record = cls.objects.get(user=user, date=date)
            return {
                "status": record.status,
                "duration": record.attendance_duration(),
                "remarks": record.remarks,
            }
        except cls.DoesNotExist:
            return {"status": "absent", "duration": timedelta(), "remarks": "No record"}