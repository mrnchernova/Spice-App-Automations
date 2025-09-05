// Jenkinsfile
pipeline {
    agent any // Где будет выполняться pipeline (any - любой доступный агент)

    // Триггеры: когда запускать pipeline
    triggers {
        // Этот триггер сработает, когда GitHub отправит webhook (настроенный ранее)
        // Он слушает события, связанные с SCM (Source Code Management), такие как push.
        // GitHub Plugin должен быть настроен на вашем Jenkins.
        githubPush() // По умолчанию запускается при push событиях, настроенных в webhook.
        // Если вы хотите триггер по Pull Request, вам может понадобиться:
        // pullRequest()
    }

    // Секреты, которые будут доступны в pipeline
    // Здесь мы получаем доступ к нашему PAT из Jenkins credentials
    environment {
        GITHUB_PAT = credentials('github-pat') // ID вашего секрета в Jenkins
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Получаем код из репозитория.
                // Используем `github-pat` для аутентификации, если репозиторий приватный.
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
                // Замените команду на вашу команду сборки
                // Пример для Node.js:
                // sh 'npm install'
                // sh 'npm run build'

                // Пример для Maven:
                // sh 'mvn clean package -DskipTests' // Собираем, но пропускаем тесты на этом этапе
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Замените команду на вашу команду запуска тестов
                // Пример для Node.js:
                // sh 'npm test'

                // Пример для Maven (тесты выполняются командой 'test'):
                // sh 'mvn test'

                // Пример для Python (pytest):
                // sh 'pytest'

                // Опционально: Если ваши тесты генерируют JUnit XML отчеты
                // JUnit Plugin должен быть установлен в Jenkins
                // post {
                //    always {
                //        junit '**/target/surefire-reports/*.xml' // Путь к отчетам Maven
                //    }
                // }
            }
        }

        // Если вам нужно обновлять статус коммита/PR в GitHub
        // stage('Update GitHub Status') {
        //     steps {
        //         echo 'Updating GitHub commit status...'
        //         // Вам может понадобиться отдельный плагин или скрипт для этого,
        //         // который использует GITHUB_PAT.
        //         // Пример использования GitHub CLI:
        //         // gh api repos/${{ github.repository }}/statuses/${{ github.sha }} \
        //         //   -H "Authorization: token ${GITHUB_PAT}" \
        //         //   -f state='success' \
        //         //   -f description='Tests passed' \
        //         //   -f context='continuous-integration/jenkins'
        //     }
        // }
    }

    post {
        // Эти блоки выполняются после завершения всех стадий (независимо от успеха)
        always {
            echo 'Pipeline finished.'
            // Очистка рабочего пространства
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
            // Например, отправить уведомление об успехе
        }
        failure {
            echo 'Pipeline failed!'
            // Например, отправить уведомление о провале
        }
        unstable {
            echo 'Pipeline completed with unstable results (e.g., failed tests but build succeeded).'
        }
    }
}
