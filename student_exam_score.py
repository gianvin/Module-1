import pandas as pd
# #Code for loading the data set
df = pd.read_csv(r"C:\Users\Gina S. Ong\Documents\byui\HelloWorld\Module 1-Data Analysis\student_exam_scores.csv")
print(df.head())

# #Code for showing all rows and columns
# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None )

# print("Full DataFRame:")
# print(df)


# #Code for creating data sets
data= {
    "student_id": ["S001", "S002", "S003", "S004", "S005",],
    "hours_studied":[8.0, 1.3, 4.0, 3.5, 9.1],
    "sleep_hours": [8.8, 8.6, 8.2, 4.8, 6.4],
    "attendance_percent": [72.1, 60.7, 73.7, 95.1, 89.8],
    "previous_scores": [45, 55, 86, 66, 71],
    "exam_score": [30.2, 25.0, 35.8, 34, 40.3]
}
df =pd.DataFrame(data)

# # # #Question 1 How many students sleep 8 hours and above

count_8_plus = (df["sleep_hours"] >= 8.0).sum()
print("Number of students with 8 hours or more:", count_8_plus)

# average number of sleep hours of students
average_sleepHours= df["sleep_hours"].mean()
print(f"Average sleep hours of students: {average_sleepHours:.1f}")


# Question number 2 Which of the student has the  highest/least /exam score/previous score/sleep hours/hours studied
#Student with the highest Exam Score
highest_exam_score_student = df.loc[df["exam_score"].idxmax()]
#code for printing the student id and the score
student_id = highest_exam_score_student["student_id"]
e_score = highest_exam_score_student["exam_score"]
print("Student with the Highest Exam Score:", student_id)
print("Exam Score:", e_score)

# student with the highest previous score
highest_previous_score_student = df.loc[df["previous_scores"].idxmax()]
#code for printing the student id and the score
student_id = highest_previous_score_student["student_id"]
p_score = highest_previous_score_student["previous_scores"]
print("Student with the Highest Previous Score:", student_id)
print("Previous Score:", p_score)

#student with the highest hours sleep

highest_hours_sleep_student = df.loc[df["sleep_hours"].idxmax()]
#code for printing the student id and the score
student_id = highest_hours_sleep_student["student_id"]
s_hours = highest_hours_sleep_student["sleep_hours"]
print("ID:", student_id)
print("Highest Number of Sleep Hours:", s_hours)

#Student with the highest Hours of Study
highest_study_hours_student = df.loc[df["sleep_hours"].idxmax()]
#code for printing the student id and the score
student_id = highest_study_hours_student["student_id"]
study_hours = highest_study_hours_student["hours_studied"]
print("ID:", student_id)
print("Highest Number of Study Hours:", study_hours)

# student with the least exam score
least_exam_score_student = df.loc[df["exam_score"].idxmin()]
#code for printing the student id and the score
student_id = least_exam_score_student ["student_id"]
le_score = least_exam_score_student["exam_score"]
print("Student with the Least Exam Score:", student_id)
print("Exam Score:", le_score)

#student with the least previous score
least_previous_score_student = df.loc[df["previous_scores"].idxmin()]
#code for printing the student id and the score
student_id = least_previous_score_student ["student_id"]
lp_score = least_previous_score_student["previous_scores"]
print("Student with the Least Previous Score:", student_id)
print("Previous Score:", lp_score)

#student with the least hours of sleep
least_sleep_hours_student = df.loc[df["sleep_hours"].idxmin()]
#code for printing the student id and the score
student_id = least_sleep_hours_student ["student_id"]
ls_hours = least_sleep_hours_student["sleep_hours"]
print("Student with the Least Sleep Hours:", student_id)
print("Sleep Hours:", ls_hours)

#student with the least hours of Study
least_study_hours_student = df.loc[df["hours_studied"].idxmin()]
#code for printing the student id and the score
student_id = least_study_hours_student["student_id"]
lstudy_hours = least_study_hours_student["hours_studied"]
print("Student with the Least Sleep Hours of Study:", student_id)
print("Sleep Hours:", lstudy_hours)

#Question 3 What is the sum of the previous scores/exam scores of the students?
total_score = df["previous_scores"].sum()
print("Total of all previous scores:", total_score)

# Total score of exam scores of students
total_score = df["exam_score"].sum()
print("Total of all exam scores:", total_score)
