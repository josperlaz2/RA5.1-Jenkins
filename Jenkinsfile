pipeline {
    agent any

    stages {
        stage('Ejecutar pruebas unitarias') {
            steps {
                sh 'python3 -m unittest test_calculadora.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizada'
        }
        success {
            echo '¡Las pruebas unitarias pasaron!'
        }
        failure {
            echo '¡Las pruebas unitarias fallaron!'
        }
    }
}
