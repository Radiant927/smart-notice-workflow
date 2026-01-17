# workflow/grouping.py

def group_student(student: dict) -> str:
    """
    根据学生信息进行分组
    """
    if student.get("role") == "班长":
        return "leader"

    if student.get("attendance_rate", 100) < 80:
        return "absent"

    return "normal"
