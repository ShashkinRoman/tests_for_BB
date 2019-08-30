from tests import authorization
from tests import create_application
from tests import create_clients
from tests import create_service
from tests import create_category
from tests import create_master

authorization.main()
create_service.main()
create_application.main()
create_clients.main()
create_category.main()
create_master.main()

# try:
#     authorization.main()
#     print('Test "authorization" completed')
# except:
#     print('Test "AUTHORIZATION" FILED')
#
# try:
#     create_service.main()
#     print('Test "create_client" completed')
# except:
#     print('Test "CREATE_CLIENT" FILED')
#
# try:
#     create_application.main()
#     print('Test "registration" completed')
# except:
#     print('Test "REGISTRATION" FILED')
#
# try:
#     create_category.main()
#     print('Test "create_client" completed')
# except:
#     print('Test "CREATE_CLIENT" FILED')
# try:
#     create_clients.main()
#     print('Test "create_client" completed')
# except:
#     print('Test "CREATE_CLIENT" FILED')
