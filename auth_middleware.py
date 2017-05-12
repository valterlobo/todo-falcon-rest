import falcon


class AuthMiddleware(object):

    def process_request(self, req, resp):

        login = req.get_header('login')
        passw = req.get_header('passw')

        challenges = ['Token type="Fernet"']

        if login is None:
            description = ('Please provide an auth login '
                           'as part of the request.')

            raise falcon.HTTPUnauthorized('Auth token required',
                                          description,
                                          challenges,
                                          href='http://docs.example.com/auth')

        if not self._token_is_valid(login, passw):
            description = ('The provided auth token is not valid. '
                           'Please request a new token and try again.')

            raise falcon.HTTPUnauthorized('Authentication required',
                                          description,
                                          challenges,
                                          href='http://docs.example.com/auth')

    def _token_is_valid(self, login, passw):
        if login == 'valter' and passw == 'valter':
            return True
        else:
            return False
