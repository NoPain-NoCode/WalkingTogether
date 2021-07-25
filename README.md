# WalkingTogether
🐶2021캡스톤디자인
## BE

### 21.07.25
- user app의 회원가입/로그인 기능 추가
- maps app의 최단거리 출력 기능 추가

#### 발생오류
`django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency users.0001_initial on database 'default'.`
- 최단거리 로직 에러