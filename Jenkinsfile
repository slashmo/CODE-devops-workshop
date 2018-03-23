pipeline {

  agent { dockerfile true }

  stages {
    stage ('List pip packages') {
      steps {
        sh 'pip list'
      }
    }

    stage ('List contents of /usr/src/app') {
      steps {
        sh 'ls -l /usr/src/app'
      }
    }
  }
}
