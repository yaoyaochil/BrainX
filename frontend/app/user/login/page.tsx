// pages/auth/login.tsx
"use client";

import {Form, Input, Button} from 'antd';
import styles from './index.module.scss';
import {router} from "next/client";
import HomeNavbar from "@/app/ui/home/navbar";
import React from "react";

export default function LoginPage() {
	async function handleSubmit(values: { account: string; password: string }) {
		const response = await fetch('/api/auth/login', {
			method: 'POST',
			headers: {'Content-Type': 'application/json'},
			body: JSON.stringify(values),
		});

		if (response.ok) {
			router.push('/space');
		} else {
			// Handle errors
		}
	}

	return (
		<div className={styles.container}>
			<div className={styles.formHeader}>
				<HomeNavbar/>
			</div>
			<div className={styles.formContainer}>
				<h2 className={styles.title}>登录</h2>
				<Form
					name="login"
					onFinish={handleSubmit}
					className={styles.form}
				>
					<Form.Item
						name="account"
						rules={[{required: true, message: '请输入你的账号!'}]}
					>
						<Input placeholder="Email" className={styles.input}/>
					</Form.Item>
					<Form.Item
						name="password"
						rules={[{required: true, message: '请输入你的密码!'}]}
					>
						<Input.Password placeholder="Password" className={styles.input}/>
					</Form.Item>
					<Form.Item>
						<Button type="primary" htmlType="submit" className={styles.loginButton}>
							登录
						</Button>
					</Form.Item>
					<Form.Item>
						<Button href="/user/register" className={styles.registerButton}>
							注册
						</Button>
					</Form.Item>
				</Form>
			</div>
		</div>
	);
}
