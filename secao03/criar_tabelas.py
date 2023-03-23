from core.configs import settings   
from core.database import engine    


async def create_tables()-> None:    
    import models.__all_models  
    print('criando as tabelas no Banco de dados')   

    async with engine.begin() as conn:  
        await conn.run_sync(settings.DBBaseMOdel.metadata.drop_all)     
        await conn.run_sync(settings.DBBaseMOdel.metadata.create_all)   
        print('Tabela criada com sucesso')  


        if __name__ == '__main__':  
            import asyncio  

            asyncio.run(create_tables())