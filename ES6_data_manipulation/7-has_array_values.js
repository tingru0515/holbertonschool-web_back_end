function hasValuesFromArray(set, arrayOfObjects) {
  return arrayOfObjects.every((element) => set.has(element));
}

export default hasValuesFromArray;
