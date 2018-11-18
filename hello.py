
import click

class Config(object):

    def __init__(self):
        self.verbose = False
        # self.home_directory = '.'


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--home_directory', type=click.Path())
@pass_config
def cli(config,verbose, home_directory):
    config.verbose = verbose
    if home_directory is None:
        home_directory = '.'
    config.home_directory = home_directory




@cli.command()
@click.option('--string', default='world',
              help='This is the thng that is greeted')
@click.option('--repeat', default=1,
              help='number of times to repeat')
@click.argument('out',type=click.File('w'), default='-',
                required=False)
@pass_config
def say(config,string, repeat, out):
    """This script greets you
        <arguments> out

    """
    # print("Hello {}".format(string))

    # click.echo(out)
    print("Home Directory : {}".format(config.home_directory))
    if config.verbose:
        click.echo("We are in verbose mode")
    for x in range(repeat):
        click.echo("Hello {}".format(string), file=out)  #  Handles Unicode better





