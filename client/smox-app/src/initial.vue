<template>
    <div>
        <transition name="fade">
            <div key="2" v-if="!loading" >
                <App />
            </div>
        </transition>
        <transition name="fade">
            <div key="1" v-if="loading">
                <LoadingScreen :progress="progress"/>
            </div>
        </transition>
    </div>
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