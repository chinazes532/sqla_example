from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select


async def set_user(tg_id, first_name, date):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id,
                             first_name=first_name,
                             date=date))
            await session.commit()
