def bob = './bob/bob.sh --verbose'

pipeline {
    agent {
        node {
            label SLAVE
        }
    }
    options {
        timestamps()
        timeout(time: 1, unit: 'HOURS')
    }
    stages {
        stage('hello-world') {
            steps {
                echo 'hello-world'
            }
        }
        stage('Prepare kubectl') {
          steps {
                writeFile file: '/tmp/ci.conf', text: '''apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUN5RENDQWJDZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRFNE1USXhNekV6TWpneU5sb1hEVEk0TVRJeE1ERXpNamd5Tmxvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBT3dZCmp3eVVXeTBiOHBrOFhmdjlEMjRBeUt4cWRCSDBSYTJGamtDYndZeHplTm4vM3dManEzbjVLSzg2cTFYMFVkTkMKQVZ5ZldrTlZzRlRTaXRFbmdndXVYZzhoLy8vVTFSOVBpNFNNdloyRnBmZzRvYUlEajNWRUdOaGFxbjlVdXhPUgpSU25STHlmY09zbFhELzhpLytGcjBQQWVoRkdteTJXM3NEaVJuMHhSSzdqcVpIa3N1YVVTQUYwK05lVlo0L0xECmxQTE50WEN3ZWdwWW1ZV1VOR0o3ZDFWM1ViNnU3M2laYXdZUVZmNWg2TTBhejNYYWJXV1lPcnRJQUsvUUNTak8Kd25PdjJTY1JhT2Q2aUFRblBLb014ZGlZUXJNMXllYVkzYzJjZ1BFdmhPZ0dQZ0YzVEVSYTVBc1Y3dk5YU3AyTQowbFNzNy9mV2xjeXJhbUdMMFlNQ0F3RUFBYU1qTUNFd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFOQjVSbW9wQnRHYnlZOC95OGtZaDRLUHNsaTYKSHRRNUkyQml0aDhHY0lsaUNzaXVkL28rempPUkh6VFlzeDdMMVpEUmMybEgwdkZKcVFxN1JuUVdXdnRkTUdDbQpmWUlBZlB6NG9Jektmc1V5bEJRY2svZkxMTGRrOVpXNGptSjN5bW8zSDF3cVBnWnVCQU9CKzJKZFI0QXFJZ3dNCmlZcWtvT0VqNjk3VEZNczBkZlZNbm9UUHEzWjZZVHQ4V3pnNFlBSVdUR3VhcmViMUFmY2pzUFpXK0pJRVZxYUsKaUR3ekZzcDNsRnZiVzNncDAvUnphVWNrd1ZKV21SbnR4K3ZnZ3IrRk94WVFtWmZDSVRKRTBiQ1lZMS95d1RzdApIMHNMSWFTb0ZuazVNVDJxV05GV3RnSURVQWxjZGpHVFZ5djlCSEJxaS8vR0RKajJSM2lITDN0YmIrZz0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=
    server: https://10.210.165.74:6443
  name: kubernetes
contexts:
- context:
    cluster: kubernetes
    user: ci-user
  name: ci-context
current-context: ci-context
kind: Config
preferences: {}
users:
- name: ci-user
  user:
    as-user-extra: {}
    token: eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImNpLXNlcnZpY2UtYWNjb3VudC10b2tlbi1rNWRneiIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJjaS1zZXJ2aWNlLWFjY291bnQiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIyYjlkOWYyZS02YzE4LTExZTktOTgwNC0wMDUwNTZiMDg2OTUiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6ZGVmYXVsdDpjaS1zZXJ2aWNlLWFjY291bnQifQ.i67LMUalEypF3Rse-UUo7MWpcdDIOMUJoGOLewU_LZjzOf4e8chmAvsTPxS1ZekqVlQWNyRb97kZWdHDQ6e6vX2f9E0oppKa23bGUPyvoiX8p8eb47G_4la1KEGg1htN6FavFPhs_u1qZQbJO8iu7RscvIj4bnJtuAj_eSG0WnV5qcwVYkPmlH_L4pJIC0dGloahXkXlA_2dELUMSM-CorQaYAtQeO_0lBUzPInwRtpsQHpFNfmzewuwt4ZP0e4OoB27Z4UVBtavYS35X45LpM7xzwk_dNyfah23gZpWa26GrAdbeMrCCYK3BapWHhg7M7Lt8MLnbR2ZguFWbuIFyg'''
          }
        }
        stage('Prepare bob') {
            steps {
                sh 'git clean -xdff --exclude=.m2 --exclude=settings.xml'
                sh 'git submodule sync'
                sh 'git submodule update --init --recursive'
                sh './bob/bob.sh --selftest'
            }
        }
        stage('Bob Lint') {
            steps {
                sh "${bob} lint"
            }
        }
        stage('Build Snapshot Docker Image & Helm Chart') {
            steps {
                sh "${bob} image"
            }
        }
        stage('Push Snapshots of Docker and Helm') {
            steps {
                sh './bob/bob.sh --verbose push'
            }
        }
    }
}