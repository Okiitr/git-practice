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

        stage('parallel') {
          steps {
            sleep 2
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

    stage('mail') {
      steps {
        mail(subject: 'jenkins', body: 'hello oman this mail is sent by jenkins', from: 'okumar@ch.iitr.ac.in', to: 'kumaroman4@gmail.com')
      }
    }

  }
}