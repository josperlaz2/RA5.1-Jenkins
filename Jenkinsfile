pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/tu_usuario/python-calculadora-ci.git' , branch: 'main'
            }
        }
        stage('Unit Test') {
            steps {
                sh 'python -m unittest test_calculadora.py'
            }
        }
    }
    post {
        always {
            echo 'Pipeline completada. Revisa los logs para detalles.'
        }
    }
}', branch: 'main'
            }
        }
        stage('Unit Test') {
            steps {
                sh 'python -m unittest test_calculadora.py'
            }
        }
    }
    post {
        always {
            echo 'Pipeline completada. Revisa los logs para detalles.'
        }
    }
}
