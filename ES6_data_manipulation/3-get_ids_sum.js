function getStudentIdsSum(arrayOfObjects) {
  return arrayOfObjects.reduce((sum, student) => sum + student.id, 0);
}

export default getStudentIdsSum;
