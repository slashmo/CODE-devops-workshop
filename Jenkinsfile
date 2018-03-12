pipeline {

  agent { dockerfile true }

  stages {
    stage ('List pip packages') {
      sh 'pip list'
    }

    stage ('List contents of /usr/src/app') {
      sh 'ls -l /usr/src/app'
    }
  }
}
