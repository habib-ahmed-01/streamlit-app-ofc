import asyncio
import asyncpg


# Adds the new rows into the DB
async def insert_data(pool, data):
    async with pool.acquire() as connection:
        query = """
        INSERT INTO ic_msz (fqdn, ip, name, os_family, dc_zone)
        VALUES ($1, $2, $3, $4, $5)
        """
        await connection.execute(query, data['fqdn'], data['ip'], data['name'], data['os_family'], data['dc_zone'])


# Deletes the rows that were selected by the user
async def delete_data(pool, data):
    async with pool.acquire() as connection:
        query = """Delete from ic_msz where id = $1"""
        await connection.execute(query, data["id"])


async def edit_data(pool, id_value, data):
    async with pool.acquire() as connection:
        set_clause = ", ".join([f"{key} = ${i + 2}" for i, key in enumerate(data)])
        query = f"""
        UPDATE ic_msz SET
            {set_clause}
            where id = $1
            """
        print(query)
        await connection.execute(query, id_value, *data.values())


# Main function that initialises connection pool
async def main(key, data_list):
    # Replace with your PostgresSQL connection details
    pool = await asyncpg.create_pool(user='ic_merck_user', password='password123#', database='merck_db',
                                     host='localhost', port='5432')

    tasks = []
    if key == 'insert':
        for entry in data_list:
            tasks.append(insert_data(pool, entry))

    elif key == 'delete':
        for entry in data_list:
            tasks.append(delete_data(pool, entry))

    elif key == 'edit':
        for entry in data_list:
            id_value = entry["id"]
            del entry["id"]
            tasks.append(edit_data(pool, id_value, entry))

    await asyncio.gather(*tasks)

    await pool.close()


# Run the async main function
def save_to_db(key, data_list):
    asyncio.run(main(key, data_list))
