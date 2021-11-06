from blackhat.a02_BASIC_NETWORKING.bh_sshRcmd import ssh_command


def test_ssh_command():
    ssh_command(
        ip='ASUS-P9-X79',
        user='thom',
        passwd='nbhgyt65',
        command='ClientConnected'
    )
