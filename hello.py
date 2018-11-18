
import click


@click.command()
@click.option('--string', default='world',
              help='This is the thng that is greeted')
@click.option('--repeat', default=1,
              help='number of times to repeat')
@click.argument('out',type=click.File('w'), default='-',
                required=False)
def cli(string, repeat, out):
    """This script greets you"""
    # print("Hello {}".format(string))

    click.echo(out)
    for x in range(repeat):
        click.echo("Hello {}".format(string))  #  Handles Unicode better





