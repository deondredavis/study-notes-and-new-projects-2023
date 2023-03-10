# Real World Data from The Ohio State University (https://courses.osu.edu/)

"""
def unique_values(data, key):
    new_unique_values = set()
    for element in data:
        if key in element:
            value = element[key]
            if value not in new_unique_values:
                new_unique_values.add(value)
    print(new_unique_values)
"""


def unique_values(data, key):
    unique_values_2 = []
    for element in data:
        if element[key] not in unique_values_2:
            unique_values_2.append(element[key])
    print(unique_values_2)


data = [
    {
        "course_name": "Calculus 1",
        "course_department": "Mathematics",
        "course_number": "1151"
    },

    {
        "course_name": "Principles of Microeconomics",
        "course_department": "Economics",
        "course_number": "2002.01"
    },

    {
        "course_name": "Symbolic Logic",
        "course_department": "Philosophy",
        "course_number": "2500"
    },

    {
        "course_name": "General Chemistry 1",
        "course_department": "Chemistry",
        "course_number": "1210"
    },

    {
        "course_name": "Introduction to Sustainability",
        "course_department": "Agricultural, Environmental, and Development Economics",
        "course_number": "2500"
    }
]

unique_values(data, "course_number")
