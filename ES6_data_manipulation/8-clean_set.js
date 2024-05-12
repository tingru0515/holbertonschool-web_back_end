function cleanSet(set, startString) {
  // Filter the set to include only values that start with startString
  const filteredValues = [...set].filter((value) => value.startsWith(startString));

  // Join the filtered values with '-' separator
  return filteredValues.join('-');
}

export default cleanSet;
