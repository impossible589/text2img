iscmdav = ""
cmd = ""

import asyncssh
import asyncio


async def run():
    try:
        global conn
        # Establish connection manually
        conn = await asyncssh.connect(
            '91.203.133.137',
            username='root',
            client_keys=['/home/gourav/e2ee'],
            passphrase='gourav',
            known_hosts=None
        )

        print("✅ Connected!")
    except Exception as e:
        print("❌ Error:", e)


async def looper():
    global iscmdav  # ✅ FIRST
    global cmd
    await run()
    while True:
        await asyncio.sleep(.5)
        #inp = input("Enter Cmd")
        #cmd = inp
        #cmd = "ls"
        #iscmdav = True

        if (iscmdav):

            iscmdav = False
            process = await conn.create_process(cmd, term_type='xterm')
            async for line in process.stdout:
                print(line, end="")


def thread_target():
    asyncio.run(looper())


# t = threading.Thread(target=thread_target)
# t.start()
def cmdmainlooper():
    while True:
        inp = input("Enter Cmd")
        cmd = inp
        iscmdav = True
# asyncio.run(looper())
