<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-16">
        <h1>Docker Manager</h1>
        <br><br>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col">Container name</th>
            <th scope="col">Status</th>
            <th scope="col">Start time</th>
            <th scope="col">Image name</th>
            <th scope="col">Up time</th>
            <th scope="col"></th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="container in containers">
            <td>{{ container.containerName }}</td>
            <td class="link-success" v-if="container.containerStatus == 'running'">
              <strong>running</strong>
            </td>
            <td class="link-warning" v-else-if="container.containerStatus == 'restarting'">
              <strong>restarting</strong>
            </td>
            <td  class="link-danger" v-else><strong>stopped</strong></td>
            <td>{{ container.startTime }}</td>
            <td>{{ container.imageName }}</td>
            <td>{{ container.upTime }}</td>
            <td></td>
            <td>
              <button type="button" class="btn btn-outline-success btn-sm"
                      v-on:click="driveContainer(command[0], container.containerName)">start</button>
              <button type="button" class="btn btn-outline-danger btn-sm"
                      v-on:click="driveContainer(command[1], container.containerName)">stop</button>
              <span>|</span>
              <button type="button" class="btn btn-outline-warning btn-sm"
                      v-on:click="driveContainer(command[2], container.containerName); getContainerList">restart</button>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'DockerContainerManager',
  data() {
    return {
      msg: '',
      containers: [],
      timer: '',
      command: ["start", "stop", "restart"],
    };
  },
  created() {
    this.getContainerList();
    this.timer = setInterval(this.getContainerList, 1000);
  },
  methods: {
    async getContainerList() {
      fetch('http://backend:8000/api/docker-qa-manage/ps')
        .then(resp => resp.json())
        .then((data) => {
          this.containers = data.containers
          // this.msg = data.containers
        })
        .catch(error => {
          this.msg = error;
        });
    },
    async driveContainer(command, containerName) {
      alert('Attention! Container '+containerName+' will be '+command+'ed.');
      fetch('http://backend:8000/api/docker-qa-manage/'+command+'/'+containerName)
        .then(resp => resp.json())
        .then((data) => {
          this.containers = data.containers
          // this.msg = data.status
          this.getContainerList()
        })
        .catch(error => {
          this.msg = error;
        });
    },
    cancelAutoUpdate () {
      clearInterval(this.timer);
    }
  },
  beforeDestroy() {
    this.cancelAutoUpdate();
  },
};
</script>
