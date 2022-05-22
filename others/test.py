# import graphviz
# from sklearn import tree
# from sklearn.datasets import load_iris

# iris = load_iris()
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(iris.data, iris.target)

# graph = graphviz.Source(tree.export_graphviz(clf, class_names=iris.feature_names, filled=True))
# graph

# graph.render('decision_tree')

# coding: utf-8
from __future__ import print_function
import sys, os
sys.path.append("c:\\VisualStudio2017\\Python3.5_GPU\\OpenAI_Gym")

from gym.spaces import *
from stable_baselines import PPO2
from stable_baselines.bench import Monitor
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
import argparse
import datetime
import gym
import numpy as np
import pybullet_envs
import time

np.set_printoptions(precision=3 , suppress=True, floatmode='fixed')

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-t', '--tbourd_log',  type=int, default=0, help='Use tensor-boards')
parser.add_argument('-l', '--laern_view',  type=int, default=0, help='View agents in learning')
parser.add_argument('-s', '--sample_view', type=int, default=0, help='Confirmation of operation by random action')
parser.add_argument('-ld','--load_view',   type=int, default=1, help='Check operation with parameters')
parser.add_argument('-e', '--env',         type=int, default=1, help='PyBullet Environment')

args = parser.parse_args()

# ログフォルダの生成
StartTime = datetime.datetime.now()
log_dir = './logs/'
os.makedirs(log_dir, exist_ok=True)

ENV_SELECT = 1 if args.env        > 10 else args.env
TBOARD_LOG  = 0 if args.tbourd_log > 1  else args.tbourd_log
LEARN_VIEW  = 0 if args.laern_view > 1  else args.laern_view
SAMPLE_VIEW = 0 if args.sample_view> 1  else args.sample_view
LOAD_VIEW   = 1 if args.load_view  > 1  else args.load_view

print("\n<< Setup parameters >>")
print("ENV_SELECT :", ENV_SELECT)
print("TBOARD_LOG  :", TBOARD_LOG )
print("LEARN_VIEW  :", LEARN_VIEW )
print("SAMPLE_VIEW :", SAMPLE_VIEW)
print("LOAD_VIEW   :", LOAD_VIEW  )


# [select game]
# 0:	env = gym.make("HumanoidBulletEnv-v0")
#		python -m pybullet_envs.examples.enjoy_TF_HumanoidBulletEnv_v0_2017may
if    ENV_SELECT == 0:
    ENV_NAME = 'HumanoidBulletEnv-v0'
    time_step = 12800000
    test_count= 100
    env = gym.make( ENV_NAME )

# 1:	env = gym.make("AntBulletEnv-v0")
#		python -m pybullet_envs.examples.enjoy_TF_AntBulletEnv_v0_2017may
elif  ENV_SELECT == 1:
    ENV_NAME = 'AntBulletEnv-v0'
    time_step = 1000000
    test_count= 100
    env = gym.make( ENV_NAME )

# 2:	env = gym.make("HalfCheetahBulletEnv-v0")
#		python -m pybullet_envs.examples.enjoy_TF_HalfCheetahBulletEnv_v0_2017may
elif  ENV_SELECT == 2:
    ENV_NAME = 'HalfCheetahBulletEnv-v0'
    time_step = int(12800000/2)
    test_count= 100
    env = gym.make( ENV_NAME )

# 3:	env = gym.make("HopperBulletEnv-v0")
#		python -m pybullet_envs.examples.enjoy_TF_HopperBulletEnv_v0_2017may
elif  ENV_SELECT == 3:
    ENV_NAME = 'HopperBulletEnv-v0'
    time_step = int(12800000/2)
    test_count= 100
    env = gym.make( ENV_NAME )

# 4:	env = gym.make("Walker2DBulletEnv-v0")
#		python -m pybullet_envs.examples.enjoy_TF_Walker2DBulletEnv_v0_2017may
elif  ENV_SELECT == 4:
    ENV_NAME = 'Walker2DBulletEnv-v0'
    time_step = int(12800000/2)
    test_count= 100
    env = gym.make( ENV_NAME )

# 5:	env = gym.make("BipedalWalker-v3")
elif  ENV_SELECT == 5:
    ENV_NAME = 'BipedalWalker-v3'
    time_step = int(12800000/100)
    test_count= 100
    env = gym.make( ENV_NAME )

# 6:	env = gym.make("Breakout-v0")
elif  ENV_SELECT == 6:
    ENV_NAME = 'Breakout-v0'
    time_step = int(12800000/2)
    test_count= 100
    env = gym.make( ENV_NAME )

# 7:	env = gym.make("ThrowerBulletEnv-v0")
# python -m pybullet_envs.examples.enjoy_TF_vThrowerBulletEnv_v0_2017may
elif  ENV_SELECT == 7:
    ENV_NAME = 'ThrowerBulletEnv-v0'
    time_step = int(12800000/2)
    test_count= 100
    env = gym.make( ENV_NAME )

# 8:	env = gym.make("MinitaurBulletEnv-v0")
elif  ENV_SELECT == 8:
    from pybullet_envs.bullet.minitaur_gym_env import MinitaurBulletEnv
    ENV_NAME = 'MinitaurBulletEnv-v0'
    time_step = int(12800000/2)
    test_count= 100
    env = MinitaurBulletEnv(render=True)

# 9:	env = gym.make("RacecarBulletEnv-v0")
elif  ENV_SELECT == 9:
    from pybullet_envs.bullet.racecarGymEnv import RacecarGymEnv
    ENV_NAME = 'RacecarBulletEnv-v0'
    time_step = int(12800000/100)
    test_count= 100
    env = RacecarGymEnv(renders=True , isDiscrete=False)

# 10:	env = gym.make("KukaBulletEnv-v0")
elif  ENV_SELECT == 10:
    from pybullet_envs.bullet.kukaGymEnv import KukaGymEnv
    ENV_NAME = 'KukaBulletEnv-v0'
    time_step = int(12800000/2)
    test_count= 100
    env = KukaGymEnv(renders=True , isDiscrete=False)

# 環境の生成
file_name = ENV_NAME + '_pybullet_model'

# 空間の出力
def print_spaces(label, space):
    # 空間の出力
    print(label, space)

    # Box/Discreteの場合は最大値と最小値も表示
    if isinstance(space, Box):
        print('    最小値: ', space.low)
        print('    最大値: ', space.high)
    if isinstance(space, Discrete):
        print('    最小値: ', 0)
        print('    最大値: ', space.n-1)


# 行動空間と状態空間の型の出力
print_spaces('行動空間: ', env.action_space)
print_spaces('状態空間: ', env.observation_space)

cnt = 0
if  (SAMPLE_VIEW == 1) or (LOAD_VIEW == 1):
    if  (SAMPLE_VIEW == 0) and (LOAD_VIEW== 1):
        env = DummyVecEnv([lambda: env])
        model = PPO2.load( file_name )

        # モデルのテスト
        env.render(mode='human')
        state = env.reset()
        while True:
            # スリープ
            time.sleep(1/60)

            # モデルの推論
            action, _ = model.predict(state)

            # 1ステップ実行
            state, reward, done, info = env.step(action)
            print("action(" , action , ") ->reward=", reward, ",done=" , done , cnt)

            cnt += 1
            # エピソード完了
            if done:
                break
    else:
        # ランダム行動による動作確認
        env.render(mode='human')
        env.reset()
        action = env.action_space.sample()
        while True:
            # スリープ
            time.sleep(1/60)

            # 1ステップ実行
            state, reward, done, info = env.step(action)
            cnt += 1
            print(cnt,",",reward)

            # エピソード完了
            if done:
                break