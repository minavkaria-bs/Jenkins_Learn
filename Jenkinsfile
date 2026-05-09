pipeline {
    agent { 
        node {
            label 'docker-agent-py'
            }
      }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd myapp
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp
                python3 hello.py
                python3 hello.py --name=Brad
                python3 hello.py --greeting=afternoon
                python3 hello.py --greeting=evening --name=Jenkins
                python3 hello.py --repeat=3
                python3 hello.py --name=Brad --shout
                python3 hello.py --name=Admin --greeting=evening --repeat=2 --shout
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
