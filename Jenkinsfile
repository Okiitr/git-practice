pipeline {
  agent any
  stages {
    stage('1st job') {
      parallel {
        stage('1st job') {
          steps {
            sleep 9
          }
        }

        stage('parllel') {
          steps {
            echo 'dfdgggf'
          }
        }

      }
    }

    stage('2nd job') {
      steps {
        sh '''pwd 
date'''
      }
    }

    stage('3rd stage') {
      steps {
        echo 'hi there'
      }
    }

  }
}