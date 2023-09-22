import grpc
import logging
import asyncio
from concurrent import futures
import team_pb2
import team_pb2_grpc

logging.basicConfig(level=logging.INFO)

class TeamServicer(team_pb2_grpc.TeamServiceServicer):
    def __init__(self):
        self.teams = []

    async def Create(self, request, context):
        team = team_pb2.Team(id=len(self.teams) + 1, task=request.task)
        self.teams.append(team)
        logging.info(f"Created Team: ID={team.id}, Task={team.task}")
        return team

    async def Read(self, request, context):
        if request.id <= len(self.teams):
            team = self.teams[request.id - 1]
            logging.info(f"Read Team: ID={team.id}, Task={team.task}")
            return team
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Team not found")
            logging.error("Read Team: Not Found")
            return team_pb2.Team()

    async def Update(self, request, context):
        if request.id <= len(self.teams):
            self.teams[request.id - 1].task = request.task
            updated_team = self.teams[request.id - 1]
            logging.info(f"Updated Todo: ID={updated_team.id}, Task={updated_team.task}")
            return updated_team
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Team not found")
            logging.error("Update Team: Not Found")
            return team_pb2.Team()

    async def Delete(self, request, context):
        if request.id <= len(self.teams):
            deleted_team = self.teams.pop(request.id - 1)
            logging.info(f"Deleted Team: ID={deleted_team.id}, Task={deleted_team.task}")
            return team_pb2.DeleteTeamResponse(success=True)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Team not found")
            logging.error("Delete Team: Not Found")
            return team_pb2.DeleteTeamResponse(success=False)

async def serve():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    team_pb2_grpc.add_TeamServiceServicer_to_server(TeamServicer(), server)
    server.add_insecure_port('[::]:50051')
    logging.info("Starting asynchronous gRPC server on port 50051...")
    await server.start()
    await server.wait_for_termination()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(serve())
