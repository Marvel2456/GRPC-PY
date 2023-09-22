import grpc
import team_pb2
import team_pb2_grpc
import logging

logging.basicConfig(level=logging.INFO)

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = team_pb2_grpc.TeamServiceStub(channel)

    # Create Team Task
    create_response = stub.Create(team_pb2.CreateTeamRequest(task="Buy Buggatti"))
    logging.info(f"Create Team Response: ID={create_response.id}, Task={create_response.task}")

    # Read Team Task
    read_response = stub.Read(team_pb2.ReadTeamRequest(id=1))
    logging.info(f"Read Team Response: ID={read_response.id}, Task={read_response.task}")

    # Update Team Task
    update_response = stub.Update(team_pb2.UpdateTeamRequest(id=1, task="Buy more Buggatti"))
    logging.info(f"Update Team Response: ID={update_response.id}, Task={update_response.task}")

    # Delete Team Task
    delete_response = stub.Delete(team_pb2.DeleteTeamRequest(id=1))
    logging.info(f"Delete Team Response: Success={delete_response.success}")

if __name__ == '__main__':
    run()
