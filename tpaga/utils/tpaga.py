import json

from client import Client


client = Client()


def test_payment_request():

    r = client.create_payment_request(
        12344,
        'https://example.com/compra/348820',
        'https://example.com/comprobante/348820',
        '5638274',
        'sede_45',
        'Compra en Tienda X',
        '61.1.224.56',
    )

    response = json.loads(r)
    res = json.dumps(response, indent=4, sort_keys=True)
    print(res)

def test_payment_confirmation():

    r = client.payment_request_confirmation(
        'pr-799e3c987257a7e87ec9ec1f242e43acc8eb94c6a7165a1b4c063da7e671bae8b2587376'
    )

    response = json.loads(r)
    res = json.dumps(response, indent=4, sort_keys=True)
    print(res)

if __name__ == '__main__':
    #test_payment_request()
    test_payment_confirmation()
