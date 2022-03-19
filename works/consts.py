NOT_STARTED_CODE = 2
IN_WORK_CODE = 1
COMPLETED_CODE = 3
NOT_STARTED = 'Не начато'
IN_WORK = 'В работе'
COMPLETED = 'Сдано'
STATUSES = (
    (NOT_STARTED_CODE, NOT_STARTED),
    (IN_WORK_CODE, IN_WORK),
    (COMPLETED_CODE, COMPLETED)
)

STATUSES_DICT = {
    NOT_STARTED_CODE: NOT_STARTED,
    IN_WORK_CODE: IN_WORK,
    COMPLETED_CODE: COMPLETED
}
