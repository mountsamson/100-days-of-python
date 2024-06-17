student_dict = {
    "student": "Angela", "James" "john"
    "score": [34,56,43]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)


# for ( key, value) in student_data_frame.items()

# print(value)

for (index, row ) in student_data_frame.iterrows():
    if row.score == "Angela":
        print(row)