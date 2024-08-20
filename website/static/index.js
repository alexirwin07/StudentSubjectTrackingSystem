function deleteGoal(goalId) {
    fetch('/delete-goal', {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ goalId: goalId })
    }).then((_res) => {
        window.location.href = "/goals";
    })
}

function deleteGrade(gradeId) {
  fetch('/delete-grade', {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ gradeId: gradeId })
  }).then((_res) => {
      window.location.href = "/";
  })
}

function deleteSubject(subjectId) {
  fetch('/delete-subject', {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ subjectId: subjectId })
  }).then((_res) => {
      window.location.href = "/subjects-grades";
  })
}