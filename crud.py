import asyncio
from sqlalchemy import select, orm
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User, db_helper, Profile, Post


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    session.add(user)
    await session.commit()
    print("Created user:", user)
    return user


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    user: User | None = await session.scalar(stmt)
    print("Fetched user:", username, user)
    return user


async def create_user_profile(session: AsyncSession,
                              user_id: int,
                              first_name: str | None = None,
                              last_name: str | None = None,
                              bio: str | None = None) -> Profile:
    profile = Profile(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        bio=bio
    )
    session.add(profile)
    await session.commit()
    print("Created profile:", profile)
    return profile


async def show_user_with_profile(session: AsyncSession, username: str) -> list[User]:
    stmt = select(User).options(orm.selectinload(User.profile)).where(User.username == username)
    users = await session.scalars(stmt)
    for user in users:
        print("User:", user)
        if user.profile:
            print("Profile:", user.profile)
        else:
            print("No profile found for user:", user.username)


async def create_posts(
        session: AsyncSession,
        user_id: int,
        *post_titles: str,
        ) -> list[Post]:
    posts = [
        Post(title=title, user_id=user_id)
        for title in post_titles
    ]
    session.add_all(posts)
    await session.commit()
    print("Created posts:", posts)
    return posts


async def main():
    async with db_helper.session_factory() as session:
        # Попробуем получить пользователей
        user_john = await get_user_by_username(session=session, username="John")
        user_sam = await get_user_by_username(session=session, username="Sam")

        # # Если пользователя нет, создаём
        if not user_john:
            user_john = await create_user(session=session, username="John")
        if not user_sam:
            user_sam = await create_user(session=session, username="Sam")

        # Создание профилей
        await create_user_profile(session=session,
                                  user_id=user_john.id,
                                  first_name="John",
                                  last_name="Doe")
        await create_user_profile(session=session,
                                  user_id=user_sam.id,
                                  first_name="Sam",
                                  last_name="Smith")

        # Вывод информации
        await show_user_with_profile(session, username="Sam")

        # Создание постов
        await create_posts(
            session,
            user_sam.id,
            "Post", "Post1", "Post2",

        )


if __name__ == "__main__":
    asyncio.run(main())
