RIZKY HARYA R 175410001

# KUBERNETES

## Istilah — Istilah pada kubernetes

1. Pod
Adalah grup container instance. Kita bisa menjalankan beberapa container (misalnya aplikasi web + Database) dalam satu pod. Antar container dalam satu pod bisa saling mengakses dengan menggunakan alamat localhost. Bisa di katakan pod seperti laptop yang kita pakai coding.

2. Node
Adalah penyebutan dari mesin-mesin yang di gunakan. Mesin ini bisa saja mesin virtual (seperti VPS atau Instance) atau fisik.

3. Service
Merupakan mekanisme untuk mengekspos pod kita ke dunia luar. Aplikasi kita yang berjalan dalam pod tidak memiliki alamat IP yang tetap. Agar bisa diakses oleh aplikasi lain atau oleh user, kita perlu alamat IP yang tetap. Service menyediakan alamat IP yang tetap, yang nantinya akan kita arahkan ke pod kita dengan menggunakan selector.

4. Label
Adalah seperangkat informasi metadata untuk mencari pod tertentu.

5. App-Test
Kita buat label app yang isinya adalah nama aplikasi. Semua container, pod, dan service yang menjadi bagian dari aplikasi test kita beri label app=test.

6. Stage-production
Label stage bisa kita gunakan untuk menentukan berbagai konfigurasi environment deployment aplikasi kita, misalnya development, testing, performancetest, securitytest, dan production

7. Jenis-frontend
kita bisa membuat label jenis aplikasi, misalnya frontend, cache, database, fileserver, dan sebagainya.

8. Selector
Adalah filtering menggunakan label. Misalnya kita ingin mencari semua instance database untuk aplikasi test yang berjalan di production.


# Membuat sebuah Deployment menggunakan Python+Flask
pastikan sudah punya image docker "rizh/rizh_img"

1. Menggunakan perintah ```kubectl create``` untuk membuat Deployment. Pod menjalankan Container berdasarkan image docker yang digunakan. Disini saya menggunakan image docker rizh/rizh-img:v2 (image ini baru saya buat, dan telah saya push ke Docker Hub). Pada Deployment ini Pod hanya memiliki 1 Container saja.

```
$ kubectl create deployment rizh-flask --image=rizh/rizh-img:v2
```
```
deployment.apps/rizh-flask created
```

2. Melihat Deployment yang telah dibuat
```
$ kubectl get deployments
```
```
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
rizh-flask   1/1     1            1          7m55s
```
3. Melihat Pod yang telah dibuatat
```
$ kubectl get pods
```
```
NAME                          READY   STATUS    RESTARTS   AGE
rizh-flask-8675f447f6-p2rj4   1/1     Running   0          9s
```

# Membuat sebuah Service

Secara default, Pod hanya bisa diakses melalui alamat IP internal di dalam cluster Kubernetes. Supaya Container python-flask bisa diakses dari luar jaringan virtual Kubernetes, saya harus ekspos Pod sebagai Service Kubernetes.

1. Ekspos Pod pada internet publik menggunakan perintah ```kubectl expose``` ```--type-LoadBalancer``` digunakan untuk ekspos Service keluar dari Cluster.
```
kubectl expose deployment rizh-flask --type=LoadBalancer --port=5000
```

2. melihat service
```
$ kubectl get services
```
```
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          15m
rizh-flask   LoadBalancer   10.96.159.100   <pending>     5000:30949/TCP   5
```

Terlihat bahwa port 5000 di expose ke port 30949

4. lihat di localhost

![](img/end1.PNG)

![](img/end2.PNG)