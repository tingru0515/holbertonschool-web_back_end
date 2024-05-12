function updateStudentGradeByCity(arrayOfObjects, city, newGrades) {
  const selectedStudents = arrayOfObjects.filter((student) => student.location === city);
  const updatedStudents = selectedStudents.map((student) => {
    const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);
    return {
      ...student, grade: matchingGrade ? matchingGrade.grade : 'N/A',
    };
  });
  return updatedStudents;
}

export default updateStudentGradeByCity;
