# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import team_pb2 as team__pb2


class TeamServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/team.TeamService/Create',
                request_serializer=team__pb2.CreateTeamRequest.SerializeToString,
                response_deserializer=team__pb2.Team.FromString,
                )
        self.Read = channel.unary_unary(
                '/team.TeamService/Read',
                request_serializer=team__pb2.ReadTeamRequest.SerializeToString,
                response_deserializer=team__pb2.Team.FromString,
                )
        self.Update = channel.unary_unary(
                '/team.TeamService/Update',
                request_serializer=team__pb2.UpdateTeamRequest.SerializeToString,
                response_deserializer=team__pb2.Team.FromString,
                )
        self.Delete = channel.unary_unary(
                '/team.TeamService/Delete',
                request_serializer=team__pb2.DeleteTeamRequest.SerializeToString,
                response_deserializer=team__pb2.DeleteTeamResponse.FromString,
                )


class TeamServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TeamServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=team__pb2.CreateTeamRequest.FromString,
                    response_serializer=team__pb2.Team.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=team__pb2.ReadTeamRequest.FromString,
                    response_serializer=team__pb2.Team.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=team__pb2.UpdateTeamRequest.FromString,
                    response_serializer=team__pb2.Team.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=team__pb2.DeleteTeamRequest.FromString,
                    response_serializer=team__pb2.DeleteTeamResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'team.TeamService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TeamService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/team.TeamService/Create',
            team__pb2.CreateTeamRequest.SerializeToString,
            team__pb2.Team.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/team.TeamService/Read',
            team__pb2.ReadTeamRequest.SerializeToString,
            team__pb2.Team.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/team.TeamService/Update',
            team__pb2.UpdateTeamRequest.SerializeToString,
            team__pb2.Team.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/team.TeamService/Delete',
            team__pb2.DeleteTeamRequest.SerializeToString,
            team__pb2.DeleteTeamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
