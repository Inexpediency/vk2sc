import soundcloud


client = soundcloud.Client(
    client_id='730679731',
    client_secret='dEtU5fGUSSHkMlDtvhG95ZccRTEB',
    username='je',
    password='k'
)
print(client.get('/me').username)
