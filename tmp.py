        # self.conv0=nn.Sequential(*[ResidualBottleneck(in_channels,in_channels) for i in range(3)],ResidualBottleneck(in_channels,out_channels*2)) #FIXME: debug
        # self.time_mlp=TimeMLP(embedding_dim=time_embedding_dim,hidden_dim=out_channels,out_dim=out_channels*2)
        # self.conv1=ResidualBottleneck(out_channels*2,out_channels) # FIXME: change