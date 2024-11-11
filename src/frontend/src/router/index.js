import Vue from 'vue';
import Router from 'vue-router';
import 'bootstrap/dist/css/bootstrap.css';
import DockerContainerManager from '../components/DockerContainerManager';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'DockerContainerManager',
      component: DockerContainerManager,
    },
  ],
});
