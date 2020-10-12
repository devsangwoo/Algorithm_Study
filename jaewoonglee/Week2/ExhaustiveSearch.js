class ExhaustiveSearch {
  constructor() {
    this.people = [];
    this.answers;
  }

  push(personArray) {
    this.people.push(personArray);
  }

  solution(problemNum, answers) {
    let result = [];
    let resultTemp = [];
    let person정답수 = 0;
    this.answers = answers;

    //정답 갯수 확인
    for (let j = 0; j < this.people.length; j++) {
      for (let i = 0; i < problemNum; i++) {
        if (this.people[j][i % this.people[j].length] === this.answers[i % this.answers.length]) {
          person정답수++;
        }
      }
      resultTemp.push([j + 1, person정답수]);
      person정답수 = 0;
    }
    console.log('정답수', resultTemp);

    // 최대값
    let maxNum;
    for (let i = 0; i < resultTemp.length; i++) {
      if (!maxNum) {
        maxNum = resultTemp[i][1];
      }
      if (maxNum < resultTemp[i][1]) {
        maxNum = resultTemp[i][1];
      }
    }
    console.log('최대값', maxNum);

    // 최대값 복수인 경우, 오름차순
    for (let i = 0; i < resultTemp.length; i++) {
      if (maxNum === resultTemp[i][1]) {
        result.push(resultTemp[i][0]);
      }
    }
    console.log('최대값 복수인 경우, 오름차순', result);

    return result;
  }
}

let exhaustiveSearch = new ExhaustiveSearch();
exhaustiveSearch.push([1, 2, 3, 4, 5]);
exhaustiveSearch.push([1, 2, 3, 4, 5]);
exhaustiveSearch.push([2, 1, 2, 3, 2, 4, 2, 5]);
exhaustiveSearch.push([2, 1, 2, 3, 2, 4, 2, 5]);
exhaustiveSearch.push([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]);
console.log('결과값', exhaustiveSearch.solution(1000, [2, 1, 3, 4, 5, 2, 5, 1]));
