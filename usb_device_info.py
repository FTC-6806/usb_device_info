#!/usr/bin/env python

import usb.core
import click

@click.command()
@click.argument('vid', required=True)
@click.argument('pid', required=True)
def usb_device_info(vid, pid):
	device = usb.core.find(idVendor=int(vid, 16), idProduct=int(pid, 16))
	click.echo(device)
	

if __name__ == '__main__':
	usb_device_info()