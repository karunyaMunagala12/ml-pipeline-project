pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main',url:' https://github.com/karunyaMunagala12/ml-pipeline-project.git'
            }
        }

        stage('Set Up Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt || true'
            }
        }

        stage('Train Model') {
            steps {
                sh './venv/bin/python train.py'
            }
        }

        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: 'model/iris_model.pkl', fingerprint: true
            }
        }
    }
}
