from sqlalchemy import create_engine


def engine_maker(user:str,password:str,port:int,database:str):
    try:
        return create_engine(f"postgresql://{user}:{password}@localhost:{port}/{database}")
    except Exception as e:
        return f"Error"
