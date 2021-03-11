<template>
    <transition name="fade">
        <LoadingScreen key=1 v-if="loading" :progress="progress"/>
        <App key=2 v-else/>
    </transition>
</template>
<script src="./initial.js"></script>
<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity 1s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>