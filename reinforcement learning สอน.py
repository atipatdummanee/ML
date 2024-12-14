import gym
import numpy as np
import matplotlib.pyplot as plt

# สร้างสภาพแวดล้อม
env = gym.make('CartPole-v1')

# พารามิเตอร์ของ Q-learning
alpha = 0.1  # Learning rate
gamma = 0.99  # Discount factor
epsilon = 1.0  # Exploration rate
epsilon_min = 0.01
epsilon_decay = 0.995

# พารามิเตอร์สำหรับการทำ Discretization
num_buckets = (1, 1, 6, 12)  # Discretize state space
num_actions = env.action_space.n

# กำหนด Q-table
Q_table = np.zeros(num_buckets + (num_actions,))

# ฟังก์ชันสำหรับการทำ Discretization ของ state space
def discretize_state(state):
    upper_bounds = [env.observation_space.high[0], 0.5, env.observation_space.high[2], np.radians(50)]
    lower_bounds = [env.observation_space.low[0], -0.5, env.observation_space.low[2], -np.radians(50)]
    ratios = [(state[i] + abs(lower_bounds[i])) / (upper_bounds[i] - lower_bounds[i]) for i in range(len(state))]
    new_state = [int(round((num_buckets[i] - 1) * ratios[i])) for i in range(len(state))]
    new_state = [min(num_buckets[i] - 1, max(0, new_state[i])) for i in range(len(state))]
    return tuple(new_state)

# การฝึกอบรม Q-learning
num_episodes = 1000
max_steps = 200
rewards = []

for episode in range(num_episodes):
    state = discretize_state(env.reset())
    total_reward = 0

    for t in range(max_steps):
        if np.random.rand() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q_table[state])

        next_state, reward, done, _ = env.step(action)
        next_state = discretize_state(next_state)
        total_reward += reward

        best_next_action = np.argmax(Q_table[next_state])
        td_target = reward + gamma * Q_table[next_state][best_next_action]
        td_error = td_target - Q_table[state][action]
        Q_table[state][action] += alpha * td_error

        state = next_state

        if done:
            break

    rewards.append(total_reward)
    epsilon = max(epsilon_min, epsilon * epsilon_decay)

    if (episode + 1) % 100 == 0:
        print(f"Episode {episode + 1}, Total Reward: {total_reward}")

print("Training finished.\n")

# การทดสอบ agent
def test_agent(num_episodes=100):
    for episode in range(num_episodes):
        state = discretize_state(env.reset())
        total_reward = 0
        done = False

        while not done:
            action = np.argmax(Q_table[state])
            state, reward, done, _ = env.step(action)
            state = discretize_state(state)
            total_reward += reward

        print(f"Episode {episode + 1}, Total Reward: {total_reward}")

test_agent()

# การวิเคราะห์ผลลัพธ์
plt.plot(rewards)
plt.xlabel('Episode')
plt.ylabel('Total Reward')
plt.show()
