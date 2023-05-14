from core.models import ClientAction


class Controller:

    rout_url: dict

    async def rout(self, collection: str, action: str, data: ClientAction):
        try:
            await self.rout_url[collection][action](data)
        except KeyError:
            raise Exception(f"Action {action} for {collection} does not exist")
