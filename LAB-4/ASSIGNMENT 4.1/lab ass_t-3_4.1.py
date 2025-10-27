def create_student_dict():
    students = {
        's1': {'full_name': 'bhavana', 'branch': 'CSE', 'SGPA': 9.5},
        's2': {'full_name': 'anitha', 'branch': 'CSE', 'SGPA': 10}
    }
    return students

def extract_student_info(student_id):
    students = create_student_dict()
    if student_id in students:
        return students[student_id]
    return None

# Example usage
s3_info = extract_student_info('s1')
print(s3_info)  # {'full_name': 'bhavana', 'branch': 'CSE', 'SGPA': 9.5}