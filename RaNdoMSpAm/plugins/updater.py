import asyncio
import os
import sys
import git
from telethon import events
from RaNdoMSpAm import random, random2, random3, random4, random5 , random6, random7, random8, random9, random10, random11, random12, random13, random14, random15, random16, random17, random18, random19, random20, random21, random22, random23, random24, random25, random26, random27, random28, random29, random30, random31, random32, random33, random34, random35, random36, random37, random38, random39, random40, DEV, HEROKU_APP_NAME, HEROKU_API_KEY
from .. import CMD_HNDLR as hl

# -- Constants -- #
IS_SELECTED_DIFFERENT_BRANCH = (
    "looks like a custom branch {branch_name} "
    "is being used:\n"
    "in this case, Updater is unable to identify the branch to be updated."
    "please check out to an official branch, and re-start the updater."
)
OFFICIAL_UPSTREAM_REPO = "https://github.com/S780821/random-ids-spam"
BOT_IS_UP_TO_DATE = "**The random X Spam** is up-to-date sur."
NEW_BOT_UP_DATE_FOUND = (
    "new update found for {branch_name}\n"
    "changelog: \n\n{changelog}\n"
    "updating your random Spam ..."
)
NEW_UP_DATE_FOUND = "New update found for {branch_name}\n" "`updating your random  Spam...`"
REPO_REMOTE_NAME = "temponame"
IFFUCI_ACTIVE_BRANCH_NAME = "master"
DIFF_MARKER = "HEAD..{remote_name}/{branch_name}"
NO_HEROKU_APP_CFGD = "no heroku application found, but a key given? 😕 "
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/master"
RESTARTING_APP = "re-starting heroku application"
# -- Constants End -- #

@random.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random2.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random3.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random4.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random5.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random6.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random7.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random8.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random9.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random10.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random11.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random12.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random13.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random14.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random15.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random16.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random17.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random18.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random19.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random20.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random21.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random22.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random23.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random24.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random25.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random26.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random27.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random28.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random29.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random30.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random31.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random32.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random33.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random34.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random35.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random36.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random37.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random38.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random39.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
@random40.on(events.NewMessage(incoming=True, pattern=r"\%supdate(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in DEV:
        text = "__ updating Your RaNdoMSpAm Userbots __\n **Type** .ping **After 5min To check I'm On !!**"
        await e.reply(text, parse_mode=None, link_preview=None)



@random.on(
    events.NewMessage(pattern="^.update", func=lambda e: e.sender_id in DEV)
)
async def updater(message):
    try:
        repo = git.Repo()
    except git.exc.InvalidGitRepositoryError as e:
        repo = git.Repo.init()
        origin = repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
        origin.fetch()
        repo.create_head(IFFUCI_ACTIVE_BRANCH_NAME, origin.refs.master)
        repo.heads.master.checkout(True)

    active_branch_name = repo.active_branch.name
    if active_branch_name != IFFUCI_ACTIVE_BRANCH_NAME:
        await message.edit(
            IS_SELECTED_DIFFERENT_BRANCH.format(branch_name=active_branch_name)
        )
        return False

    try:
        repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
    except Exception as e:
        print(e)

    temp_upstream_remote = repo.remote(REPO_REMOTE_NAME)
    temp_upstream_remote.fetch(active_branch_name)

    changelog = generate_change_log(
        repo,
        DIFF_MARKER.format(
            remote_name=REPO_REMOTE_NAME, branch_name=active_branch_name
        ),
    )

    if not changelog:
        await message.edit("`Updation in Progress......`")
        await asyncio.sleep(5)

    message_one = NEW_BOT_UP_DATE_FOUND.format(
        branch_name=active_branch_name, changelog=changelog
    )
    message_two = NEW_UP_DATE_FOUND.format(branch_name=active_branch_name)

    if len(message_one) > 4095:
        with open("change.log", "w+", encoding="utf8") as out_file:
            out_file.write(str(message_one))
        await random.send_message(
            message.chat_id, document="change.log", caption=message_two
        )
        os.remove("change.log")
    else:
        await message.edit(message_one)

    temp_upstream_remote.fetch(active_branch_name)
    repo.git.reset("--hard", "FETCH_HEAD")

    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if len(heroku_applications) >= 1:
            if HEROKU_APP_NAME is not None:
                heroku_app = None
                for i in heroku_applications:
                    if i.name == HEROKU_APP_NAME:
                        heroku_app = i
                if heroku_app is None:
                    await message.edit(
                        "Invalid APP Name. Please set the name of your bot in heroku in the var `HEROKU_APP_NAME.`"
                    )
                    return
                heroku_git_url = heroku_app.git_url.replace(
                    "https://", "https://api:" + HEROKU_API_KEY + "@"
                )
                if "heroku" in repo.remotes:
                    remote = repo.remote("heroku")
                    remote.set_url(heroku_git_url)
                else:
                    remote = repo.create_remote("heroku", heroku_git_url)
                asyncio.get_event_loop().create_task(
                    deploy_start(random, message, HEROKU_GIT_REF_SPEC, remote)
                )

            else:
                await message.edit(
                    "Please create the var `HEROKU_APP_NAME` as the key and the name of your bot in heroku as your value."
                )
                return
        else:
            await message.edit(NO_HEROKU_APP_CFGD)
    else:
        await message.edit("No heroku api key found in `HEROKU_API_KEY` var")


def generate_change_log(git_repo, diff_marker):
    out_put_str = ""
    d_form = "%d/%m/%y"
    for repo_change in git_repo.iter_commits(diff_marker):
        out_put_str += f"•[{repo_change.committed_datetime.strftime(d_form)}]: {repo_change.summary} <{repo_change.author}>\n"
    return out_put_str


async def deploy_start(random, message, refspec, remote):
    await message.edit(RESTARTING_APP)
    await message.edit(
        "__Updated your random X Spam successfully sur__ !!!\n\n © @randomX"
    )
    await remote.push(refspec=refspec)
    await random.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
