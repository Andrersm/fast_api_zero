from fast_api.database import get_session
from sqlalchemy.orm import Session


def test_get_session():
    session_generator = get_session()
    session = next(session_generator)

    try:
        assert isinstance(session, Session)

    finally:
        session.close()
